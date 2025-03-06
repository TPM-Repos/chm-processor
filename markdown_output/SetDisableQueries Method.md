       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDisableQueries Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : SetDisableQueries Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_this_
    The [ISettingsManager](topic442.md) to disable queries upon.

_settingValue_
    The new value of the setting.

Glossary Item Box

Sets the value of the Disable Queries setting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Sub SetDisableQueries( _
       ByVal _this_ As [ISettingsManager](topic442.md), _
       ByVal _settingValue_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim this As [ISettingsManager](topic442.md)
    Dim settingValue As Boolean
     
    [Extensions](topic814.md).SetDisableQueries(this, settingValue)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static void SetDisableQueries( 
       [ISettingsManager](topic442.md) _this_ ,
       bool _settingValue_
    )  
  
#### Parameters

 _this_
    The [ISettingsManager](topic442.md) to disable queries upon.
_settingValue_
    The new value of the setting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)


