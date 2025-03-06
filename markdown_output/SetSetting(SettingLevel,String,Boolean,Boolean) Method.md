![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetSetting(SettingLevel,String,Boolean,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic458.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) > [SetSetting Method](topic454.md) : SetSetting(SettingLevel,String,Boolean,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_level_
    The level at which to save the setting.

_settingName_
    The full name of the setting, e.g. "Common\MyValue".

_settingValue_
    The value to save.

_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

Glossary Item Box

Saves the specified setting. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub SetSetting( _
       ByVal _level_ As [SettingLevel](topic661.md), _
       ByVal _settingName_ As String, _
       ByVal _settingValue_ As Boolean, _
       ByVal _preventRedirection_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim level As [SettingLevel](topic661.md)
    Dim settingName As String
    Dim settingValue As Boolean
    Dim preventRedirection As Boolean
     
    instance.SetSetting(level, settingName, settingValue, preventRedirection)  
  
C#|   
---|---  
      
    
    void SetSetting( 
       [SettingLevel](topic661.md) _level_ ,
       string _settingName_ ,
       bool _settingValue_ ,
       bool _preventRedirection_
    )  
  
#### Parameters

 _level_
    The level at which to save the setting.
_settingName_
    The full name of the setting, e.g. "Common\MyValue".
_settingValue_
    The value to save.
_preventRedirection_
    True to prevent automatic redirection if redirection is turned on.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)   
[Overload List](topic454.md)

©2024 DriveWorks Ltd. All Rights Reserved.
