![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RequiredStatesAttribute Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13907.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [RequiredStatesAttribute Class](topic13901.md) : RequiredStatesAttribute Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_states_
    The list of application states the application is required to be in for this entity to be visible.

Glossary Item Box

Creates a new instance of the [RequiredStatesAttribute](topic13901.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal ParamArray _states_() As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim states() As String
     
    Dim instance As New [RequiredStatesAttribute](topic13901.md)(states)  
  
C#|   
---|---  
      
    
    public RequiredStatesAttribute( 
       params string[] _states_
    )  
  
#### Parameters

 _states_
    The list of application states the application is required to be in for this entity to be visible.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RequiredStatesAttribute Class](topic13901.md)   
[RequiredStatesAttribute Members](topic13902.md)

©2024 DriveWorks Ltd. All Rights Reserved.
