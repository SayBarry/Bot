import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '7393252205:AAG55M3Zv9cOnTVoHS3a3FDlMOzxVVAqPf4'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '6440962840'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == '':
		bot.reply_to(message, "❌ 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧")
		return
	bot.reply_to(message,"𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐭𝐱𝐭 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == '':
		bot.reply_to(message, "❌ 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧")
		return
	dd = 0
	live = 0
	ch = 0
	ccn = 0
	cvv = 0
	lowfund = 0
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 □□■■□□").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='STOP ✅')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				if 'risk' in last:
					last='declined'
				elif 'Duplicate' in last:
					last='Approved'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➪ {last} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝘾𝙃𝘼𝙍𝙂𝙀𝘿 ➪ [ {ch} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ➪ [ {ccn} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝘾𝙑𝙑 ➪ [ {cvv} ] •", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• 𝙇𝙊𝙒 𝙁𝙐𝙉𝘿𝙎 ➪ [ {lowfund} ] •", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ➪ [ {dd} ] •", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 ➪ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, cm6, cm7, cm8, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 ◦◦◦◦
𝐁𝐲 ➪ <a href="tg://user?id=6440962840">B A R R Y</a> ''', reply_markup=mes)
				msg = f''' 
┌────────── •✧		
┃★ 𝘾𝙃𝘼𝙍𝙂𝙀𝘿 $0.5 ★〔<a href="tg://user?id=6440962840">ϟ</a>〕
└───── •✧
<a href="tg://user?id=6440962840">┌───── •✧✧• ─────┐</a>
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐀𝐑𝐃 : <code>{cc}</code>
<a href="tg://user?id=6440962840">☛</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 : Payment Successful 💘
<a href="tg://user?id=6440962840">☛</a> 𝐈𝐧𝐟𝐨 : {cc[:6]}-{card_type} - {brand}
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : {country} - {country_flag}
<a href="tg://user?id=6440962840">☛</a> 𝐁𝐚𝐧𝐤 : {bank}
<a href="tg://user?id=6440962840">☛</a> 𝐓𝐢𝐦𝐞 : 1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝
<a href="tg://user?id=6440962840">└───── •✧✧• ─────┘</a>
𝑪𝒉𝒆𝒄𝒌𝒆𝒅 𝑩𝒚 <a href="tg://user?id=6440962840">B A R R Y </a> [𝙁𝙧𝙚𝙚] '''
				print(last)
				if 'Thank' in last or 'thank' in last or 'Paid' in last or 'paid' in last:
					ch += 1
					bot.reply_to(message, msg)
				elif 'Your card does not support this type of purchase' in last:
				    msg = f''' 
┌────────── •✧		
┃★ 𝘾𝙑𝙑 $0.5 ★〔<a href="tg://user?id=6440962840">ϟ</a>〕
└───── •✧
<a href="tg://user?id=6440962840">┌───── •✧✧• ─────┐</a>
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐀𝐑𝐃 : <code>{cc}</code>
<a href="tg://user?id=6440962840">☛</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 : Payment Successful 💘
<a href="tg://user?id=6440962840">☛</a> 𝐈𝐧𝐟𝐨 : {cc[:6]}-{card_type} - {brand}
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : {country} - {country_flag}
<a href="tg://user?id=6440962840">☛</a> 𝐁𝐚𝐧𝐤 : {bank}
<a href="tg://user?id=6440962840">☛</a> 𝐓𝐢𝐦𝐞 : 1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝
<a href="tg://user?id=6440962840">└───── •✧✧• ─────┘</a>
𝑪𝒉𝒆𝒄𝒌𝒆𝒅 𝑩𝒚 <a href="tg://user?id=6440962840">B A R R Y </a> [𝙁𝙧𝙚𝙚] '''
				    cvv += 1
				    bot.reply_to(message, msg)				    
				elif 'security code is incorrect' in last or 'security code is invalid' in last:
					msg = f'''	
┌────────── •✧		
┃★ 𝘾𝙉𝙉 $0.5 ★〔<a href="tg://user?id=6440962840">ϟ</a>〕
└───── •✧
<a href="tg://user?id=6440962840">┌───── •✧✧• ─────┐</a>
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐀𝐑𝐃 : <code>{cc}</code>
<a href="tg://user?id=6440962840">☛</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 : Payment Successful 💘
<a href="tg://user?id=6440962840">☛</a> 𝐈𝐧𝐟𝐨 : {cc[:6]}-{card_type} - {brand}
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : {country} - {country_flag}
<a href="tg://user?id=6440962840">☛</a> 𝐁𝐚𝐧𝐤 : {bank}
<a href="tg://user?id=6440962840">☛</a> 𝐓𝐢𝐦𝐞 : 1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝
<a href="tg://user?id=6440962840">└───── •✧✧• ─────┘</a>
𝑪𝒉𝒆𝒄𝒌𝒆𝒅 𝑩𝒚 <a href="tg://user?id=6440962840">B A R R Y</a> [𝙁𝙧𝙚𝙚] '''
					ccn += 1
					bot.reply_to(message, msg)
				elif 'insufficient funds' in last:
					msg = f'''			
┌────────── •✧		
┃★ 𝙄𝙉𝙎𝙐𝙁𝙁𝙄𝘾𝙄𝙀𝙉𝙏 𝙁𝙐𝙉𝘿𝙎 $0.5 ★〔<a href="tg://user?id=6440962840">ϟ</a>〕
└───── •✧
<a href="tg://user?id=6440962840">┌───── •✧✧• ─────┐</a>
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐀𝐑𝐃 : <code>{cc}</code>
<a href="tg://user?id=6440962840">☛</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 : Payment Successful 💘
<a href="tg://user?id=6440962840">☛</a> 𝐈𝐧𝐟𝐨 : {cc[:6]}-{card_type} - {brand}
<a href="tg://user?id=6440962840">☛</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 : {country} - {country_flag}
<a href="tg://user?id=6440962840">☛</a> 𝐁𝐚𝐧𝐤 : {bank}
<a href="tg://user?id=6440962840">☛</a> 𝐓𝐢𝐦𝐞 : 1{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝
<a href="tg://user?id=6440962840">└───── •✧✧• ─────┘</a>
𝑪𝒉𝒆𝒄𝒌𝒆𝒅 𝑩𝒚 <a href="tg://user?id=6440962840">B A R R Y </a> [𝙁𝙧𝙚𝙚] '''
					lowfund += 1
					bot.reply_to(message, msg)	
				else:
					dd += 1
					time.sleep(5)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝘾𝙃𝙀𝘾𝙆𝙀𝘿 ✅')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("+-----------------------------------------------------------------+")
bot.infinity_polling(timeout=10, long_polling_timeout = 5)