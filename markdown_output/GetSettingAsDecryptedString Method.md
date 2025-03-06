![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetSettingAsDecryptedString Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : GetSettingAsDecryptedString Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_this_
    The [ISettingsManager](topic442.md) from which to get the decrypted string setting.

_level_
    The level from which to load the setting.

_settingName_
    The full name of the setting, e.g. "Common\MyValue".

_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

Glossary Item Box

Gets the specified setting as a string by using the data protection API to decrypt the value stored in the registry. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Function GetSettingAsDecryptedString( _
       ByVal _this_ As [ISettingsManager](topic442.md), _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _preventRedirection_ As Boolean _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim this As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim preventRedirection As Boolean
    Dim value As String
     
    value = [Extensions](topic814.md).GetSettingAsDecryptedString(this, level, settingName, preventRedirection)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static string GetSettingAsDecryptedString( 
       [ISettingsManager](topic442.md) _this_ ,
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       bool _preventRedirection_
    )  
  
#### Parameters

 _this_
    The [ISettingsManager](topic442.md) from which to get the decrypted string setting.
_level_
    The level from which to load the setting.
_settingName_
    The full name of the setting, e.g. "Common\MyValue".
_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

#### Return Value

A null reference (Nothing in Visual Basic) if the setting doesn't exist, otherwise the value of the setting.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)


