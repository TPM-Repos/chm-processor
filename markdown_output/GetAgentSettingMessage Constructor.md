![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAgentSettingMessage Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10055.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Messaging Namespace](topic10038.md) > [GetAgentSettingMessage Class](topic10049.md) : GetAgentSettingMessage Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_settingName_
    The name of the setting to get the value of.

Glossary Item Box

Creates a new instance of the [GetAgentSettingMessage](topic10049.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _settingName_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim settingName As String
     
    Dim instance As New [GetAgentSettingMessage](topic10049.md)(settingName)  
  
C#|   
---|---  
      
    
    public GetAgentSettingMessage( 
       string _settingName_
    )  
  
#### Parameters

 _settingName_
    The name of the setting to get the value of.

# ![](dotnetimages/collapse.gif)Remarks

see [StandardAgentSettingNames](topic10088.md) for collection of standard setting names that can be used.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GetAgentSettingMessage Class](topic10049.md)   
[GetAgentSettingMessage Members](topic10050.md)

©2024 DriveWorks Ltd. All Rights Reserved.
