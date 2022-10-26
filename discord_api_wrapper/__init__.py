import requests, aiohttp, asyncio
class DiscordAPI:
    def __init__(self, token: str=None):
        self.token = token
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        self.base_url = "https://discord.com/api/v9"
        
    def get_user(self, user_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/users/{user_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False
            
        
    def get_guild(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_channel(self, channel_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/channels/{channel_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_message(self, channel_id: int, message_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/channels/{channel_id}/messages/{message_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_webhook(self, webhook_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/webhooks/{webhook_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_webhook_with_token(self, webhook_id: int, webhook_token: str) -> bool:
        try:
            r = requests.get(f"{self.base_url}/webhooks/{webhook_id}/{webhook_token}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_invite(self, invite_code: str) -> bool:
        try:
            r = requests.get(f"{self.base_url}/invites/{invite_code}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_application(self, application_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/oauth2/applications/{application_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False
            
    def send_message(self, channel_id: int, content: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/messages", headers=self.headers, json={"content": content})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def send_message_with_embed(self, channel_id: int, content: str, embed: dict) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/messages", headers=self.headers, json={"content": content, "embed": embed})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def kick_user(self, guild_id: int, user_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/guilds/{guild_id}/members/{user_id}", headers=self.headers)
            if r.status_code == 204:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def ban_user(self, guild_id: int, user_id: int) -> bool:
        try:
            r = requests.put(f"{self.base_url}/guilds/{guild_id}/bans/{user_id}", headers=self.headers)
            if r.status_code == 204:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def unban_user(self, guild_id: int, user_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/guilds/{guild_id}/bans/{user_id}", headers=self.headers)
            if r.status_code == 204:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
            
        
    def create_text_channel(self, guild_id: int, name: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/guilds/{guild_id}/channels", headers=self.headers, json={"name": name, "type": 0})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_voice_channel(self, guild_id: int, name: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/guilds/{guild_id}/channels", headers=self.headers, json={"name": name, "type": 2})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_category(self, guild_id: int, name: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/guilds/{guild_id}/channels", headers=self.headers, json={"name": name, "type": 4})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_role(self, guild_id: int, name: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/guilds/{guild_id}/roles", headers=self.headers, json={"name": name})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_webhook(self, channel_id: int, name: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/webhooks", headers=self.headers, json={"name": name})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_invite(self, channel_id: int, max_age: int, max_uses: int, temporary: bool, unique: bool) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/invites", headers=self.headers, json={"max_age": max_age, "max_uses": max_uses, "temporary": temporary, "unique": unique})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_guild(self, name: str, region: str, icon: str, verification_level: int, default_message_notifications: int, explicit_content_filter: int) -> bool:
        try:
            r = requests.post(f"{self.base_url}/guilds", headers=self.headers, json={"name": name, "region": region, "icon": icon, "verification_level": verification_level, "default_message_notifications": default_message_notifications, "explicit_content_filter": explicit_content_filter})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def rename_guild(self, guild_id: int, name: str) -> bool:
        try:
            r = requests.patch(f"{self.base_url}/guilds/{guild_id}", headers=self.headers, json={"name": name})
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guild_channels(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}/channels", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guild_roles(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}/roles", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guild_bans(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}/bans", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guild_invites(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}/invites", headers=self.headers)
            if r.status_code == 200:
                if r.text == "[]":
                    return None
                else:
                    return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False
        

    def get_guild_webhooks(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}/webhooks", headers=self.headers)
            if r.status_code == 200:
                if r.text == "[]":
                    return None
                else:
                    return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guild(self, guild_id: int) -> bool:
        try:
            r = requests.get(f"{self.base_url}/guilds/{guild_id}", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def get_guilds(self) -> bool:
        try:
            r = requests.get(f"{self.base_url}/users/@me/guilds", headers=self.headers)
            if r.status_code == 200:
                return r.json()
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_channel(self, channel_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/channels/{channel_id}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_message(self, channel_id: int, message_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/channels/{channel_id}/messages/{message_id}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_messages(self, channel_id: int, message_ids: list) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/messages/bulk-delete", headers=self.headers, json={"messages": message_ids})
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_role(self, guild_id: int, role_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/guilds/{guild_id}/roles/{role_id}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_invite(self, invite_code: str) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/invites/{invite_code}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_webhook(self, webhook_id: int) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/webhooks/{webhook_id}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_webhook_with_token(self, webhook_id: int, webhook_token: str) -> bool:
        try:
            r = requests.delete(f"{self.base_url}/webhooks/{webhook_id}/{webhook_token}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def is_token_valid(self) -> bool:
        try:
            r = requests.get(f"{self.base_url}/users/@me", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def redeem_nitro(self, code: str) -> bool:
        try:
            r = requests.post(f"{self.base_url}/entitlements/gift-codes/{code}/redeem", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def is_invite_valid(self, invite_code: str) -> bool:
        try:
            r = requests.get(f"{self.base_url}/invites/{invite_code}", headers=self.headers)
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def create_thread(self, channel_id: int, name: str, type: int = 11) -> bool:
        try:
            r = requests.post(f"{self.base_url}/channels/{channel_id}/threads", headers=self.headers, json={"name": name, "type": type})
            if r.status_code == 200:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

class AsyncDiscordAPI:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://discord.com/api/v9"
        self.headers = {"Authorization": f"Bot {self.token}"}

    async def get_user(self, user_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/users/{user_id}", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_channel(self, channel_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/channels/{channel_id}", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_channels(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/channels", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_roles(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/roles", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_bans(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/bans", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_invites(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/invites", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_webhooks(self, guild_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/webhooks", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def create_guild(self, name: str, region: str, icon: str = None, verification_level: int = 0, default_message_notifications: int = 0, explicit_content_filter: int = 0, roles: list = None, channels: list = None) -> bool:
        try:
            json = {"name": name, "region": region, "verification_level": verification_level, "default_message_notifications": default_message_notifications, "explicit_content_filter": explicit_content_filter}
            if icon:
                json.update({"icon": icon})
            if roles:
                json.update({"roles": roles})
            if channels:
                json.update({"channels": channels})
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.base_url}/guilds", headers=self.headers, json=json) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_member(self, guild_id: int, user_id: int) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/members/{user_id}", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def get_guild_members(self, guild_id: int, limit: int = 1, after: int = 0) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/guilds/{guild_id}/members?limit={limit}&after={after}", headers=self.headers) as r:
                    if r.status == 200:
                        return await r.json()
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def is_token_valid(self) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/users/@me", headers=self.headers) as r:
                    if r.status == 200:
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

        
    async def redeem_nitro(self, code: str) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.base_url}/entitlements/gift-codes/{code}/redeem", headers=self.headers) as r:
                    if r.status == 200:
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            return False
            

    async def is_invite_valid(self, invite: str) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/invites/{invite}", headers=self.headers) as r:
                    if r.status == 200:
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            return False

    async def create_thread(self, channel_id: int, name: str, type=11) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"{self.base_url}/channels/{channel_id}/threads", headers=self.headers, json={"name": name, "type": type}) as r:
                    if r.status == 200:
                        return True
                    else:
                        return False
        except Exception as e:
            print(e)
            return False
