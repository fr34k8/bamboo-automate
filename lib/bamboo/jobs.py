import logging
from .. import requests

def get_jobs(conn, plan_id, sort_by_title=False):
  params = {
      "buildKey": plan_id
      }
  res = requests.get_ui_return_html(
      conn,
      conn.baseurl+'/chain/admin/config/editChainDetails.action',
      params)

  root = res #.getroot()

  jobs = {}
  li_jobkeys = root.findall('.//li[@data-job-key]')
  for li in li_jobkeys:
    key = li.attrib['data-job-key']
    edit_link = li.find('.//a').attrib['href']
    del_link = None
    title = li.find('.//a').text
    description = None
    try:
      description = li.attrib['title']
    except:
      pass

    if sort_by_title:
      jobs[title] = (key, description, edit_link, del_link,)
    else:
      jobs[key] = (title, description, edit_link, del_link,)

  return jobs