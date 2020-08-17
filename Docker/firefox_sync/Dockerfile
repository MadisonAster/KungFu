###############MAIN################
FROM ubuntu:latest
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
###################################


##########SETUP FIREFOX############
RUN add-apt-repository -y ppa:mozillateam/firefox-next
RUN apt-get update && apt-get install -y firefox && rm -rf /var/lib/apt/lists/*
RUN firefox -CreateProfile "headless /moz-headless"  -headless
COPY ./_config/_firefoxprofile/ /moz-headless
COPY ./_config/_firefoxprofile/ /_firefoxprofile
###################################



##########RUN CRON JOBS############
RUN chmod 0744 /etc/cron.d/crontest.sh
RUN crontab /etc/cron.d/crontest.sh
###################################


########RUN FIREFOX && CRON########
#CMD cron && firefox -P headless -headless >> /mnt/w/_logs/firefox.log 
#CMD firefox -P headless -headless --first-startup >> /mnt/w/_logs/firefox.log 
CMD cron -f
###################################

