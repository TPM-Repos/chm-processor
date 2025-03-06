![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic951.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPage Class](topic935.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The host application.

_settingsManager_
    The settings manager.

Glossary Item Box

Initializes the page with core objects. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Initialize( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _settingsManager_ As [ISettingsManager](topic442.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SettingsPage](topic935.md)
    Dim application As [IApplication](topic24.md)
    Dim settingsManager As [ISettingsManager](topic442.md)
     
    instance.Initialize(application, settingsManager)  
  
C#|   
---|---  
      
    
    public void Initialize( 
       [IApplication](topic24.md) _application_ ,
       [ISettingsManager](topic442.md) _settingsManager_
    )  
  
#### Parameters

 _application_
    The host application.
_settingsManager_
    The settings manager.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SettingsPage Class](topic935.md)   
[SettingsPage Members](topic936.md)

©2024 DriveWorks Ltd. All Rights Reserved.
