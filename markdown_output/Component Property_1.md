![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Component Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12454.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [RegenerateAndOverwriteComponentTask Class](topic12446.md) : Component Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the component that'll be marked for generation and have its overwrite flag set. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Component As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [RegenerateAndOverwriteComponentTask](topic12446.md)
    Dim value As String
     
    instance.Component = value
     
    value = instance.Component  
  
C#|   
---|---  
      
    
    public string Component {get; set;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This value is either the Globally Unique Identifier (GUID) or the Target Path of a released component.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RegenerateAndOverwriteComponentTask Class](topic12446.md)   
[RegenerateAndOverwriteComponentTask Members](topic12447.md)

©2024 DriveWorks Ltd. All Rights Reserved.
