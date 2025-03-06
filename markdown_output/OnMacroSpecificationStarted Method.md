![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnMacroSpecificationStarted Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7246.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [ProjectExtender Class](topic7232.md) : OnMacroSpecificationStarted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reason_
    

Glossary Item Box

Called by DriveWorks when one of the DriveWorks_OnNew, DriveWorks_OnEdit, or DriveWorks_OnCopy macros is executed. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnMacroSpecificationStarted( _
       ByVal _reason_ As [SpecificationType](topic10772.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectExtender](topic7232.md)
    Dim reason As [SpecificationType](topic10772.md)
     
    instance.OnMacroSpecificationStarted(reason)  
  
C#|   
---|---  
      
    
    protected virtual void OnMacroSpecificationStarted( 
       [SpecificationType](topic10772.md) _reason_
    )  
  
#### Parameters

 _reason_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectExtender Class](topic7232.md)   
[ProjectExtender Members](topic7233.md)

©2024 DriveWorks Ltd. All Rights Reserved.
