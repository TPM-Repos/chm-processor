![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SettingChangedEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5295.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SettingChangedEventArgs Class](topic5288.md) : SettingChangedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_settingName_
    The name of the setting that was changed.

_settingValue_
    The new value of the setting that was changed.

Glossary Item Box

Initializes a new instance of the [SettingChangedEventArgs](topic5288.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _settingName_ As String, _
       ByVal _settingValue_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim settingName As String
    Dim settingValue As String
     
    Dim instance As New [SettingChangedEventArgs](topic5288.md)(settingName, settingValue)  
  
C#|   
---|---  
      
    
    public SettingChangedEventArgs( 
       string _settingName_ ,
       string _settingValue_
    )  
  
#### Parameters

 _settingName_
    The name of the setting that was changed.
_settingValue_
    The new value of the setting that was changed.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SettingChangedEventArgs Class](topic5288.md)   
[SettingChangedEventArgs Members](topic5289.md)

©2024 DriveWorks Ltd. All Rights Reserved.
