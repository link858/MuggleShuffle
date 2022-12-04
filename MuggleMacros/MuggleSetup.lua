
SLASH_HELLO1 = "/mugglemacrosetup"
SLASH_HELLO2 = "/mmsetup"


-- /macro setup
local function MakeMacros()
    message('Macros Have Been Setup\nType /mmdel to remove them')
    
    CreateMacro("Sov", "INV_Misc_QuestionMark", "#showtooltip Sovereign Twilight Opal\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Sovereign Twilight Opal\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Veil", "INV_Misc_QuestionMark", "#showtooltip Veiled Monarch Topaz\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Veiled Monarch Topaz\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Etch", "INV_Misc_QuestionMark", "#showtooltip Etched Monarch Topaz\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Etched Monarch Topaz\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Endur", "INV_Misc_QuestionMark", "#showtooltip Enduring Forest Emerald\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Enduring Forest Emerald\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Viv", "INV_Misc_QuestionMark", "#showtooltip Vivid Forest Emerald\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Vivid Forest Emerald\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Solid", "INV_Misc_QuestionMark", "#showtooltip Solid Sky Sapphire\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Solid Sky Sapphire\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Blood", "INV_Misc_QuestionMark", "#showtooltip Bloodstone Band\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Bloodstone Band\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Sun", "INV_Misc_QuestionMark", "#showtooltip Sun Rock Ring\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Sun Rock Ring\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Cit", "INV_Misc_QuestionMark", "#showtooltip Crystal Citrine Necklace\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Crystal Citrine Necklace\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Chal", "INV_Misc_QuestionMark", "#showtooltip Crystal Chalcedony Amulet\n/cast Jewelcrafting\n/run for i=1,GetNumTradeSkills() do if GetTradeSkillInfo(i)==\"Crystal Chalcedony Amulet\" then CloseTradeSkill() DoTradeSkill(i) break end end", false)
    CreateMacro("Saro", "INV_Misc_QuestionMark", "#showtooltip Saronite Ore\n/run SELECTED_CHAT_FRAME:Clear()\n/cast Prospecting\n/use Saronite Ore", false)
    CreateMacro("Earth", "INV_Misc_QuestionMark", "#showtooltip\n/use Eternal Earth", false)
  

    -- Create new Chat Window
    local Frame = FCF_OpenNewWindow("Loots")
        ChatFrame_RemoveAllMessageGroups(Frame)
        ChatFrame_RemoveAllChannels(Frame)
        ChatFrame_AddMessageGroup(Frame, "LOOT")
        -- ChatFrame_AddMessageGroup(Frame, "OFFICER")
        
        -- Frame:SetPoint('BOTTOMLEFT', UIParent, 300, 300)
	    -- Frame:SetSize(400, 20)
        -- FCF_SavePositionAndDimensions(Frame)
        Frame:SetSize(440, 52)
        FCF_SetChatWindowFontSize(nil, Frame, 18)
	    FCF_SetWindowAlpha(Frame, 100)
        FCF_UnDockFrame(Frame)
		Frame:ClearAllPoints();
		Frame:SetPoint("CENTER", "UIParent", "CENTER", 0, 0);
		FCF_SetTabPosition(Frame, 0);
        FCF_SetLocked(Frame, false);
        Frame:AddMessage('Move Me Anywhere')
        Frame:AddMessage('DONT RESIZE ME', 0.99, 0.11, 0.21)
		Frame:Show()
end



SlashCmdList["HELLO"] = MakeMacros

local function DestroyMacros(msg)
	-- work the magic
    message('Macros Have Been Deleted')
    DeleteMacro("Blood") 
    DeleteMacro("Sun") 
    DeleteMacro("Cit")
    DeleteMacro("Chal")
    DeleteMacro("Sov") 
    DeleteMacro("Veil")
    DeleteMacro("Etch")
    DeleteMacro("Endur")
    DeleteMacro("Viv")
    DeleteMacro("Solid")
    DeleteMacro("Saro")
    DeleteMacro("Earth")
    
end


SLASH_BIDS1 = '/muggledelete'
SLASH_BIDS2 = '/muggledel'
SLASH_BIDS3 = '/mmdel'
SlashCmdList.BIDS = DestroyMacros
