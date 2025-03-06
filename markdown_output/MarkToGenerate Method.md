![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MarkToGenerate Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3265.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupReleasedComponents Class](topic3238.md) : MarkToGenerate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentTargetPath_
    The full path to the released component to update.

Glossary Item Box

Marks the specified component as requiring generation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub MarkToGenerate( _
       ByVal _componentTargetPath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupReleasedComponents](topic3238.md)
    Dim componentTargetPath As String
     
    instance.MarkToGenerate(componentTargetPath)  
  
C#|   
---|---  
      
    
    public void MarkToGenerate( 
       string _componentTargetPath_
    )  
  
#### Parameters

 _componentTargetPath_
    The full path to the released component to update.

# ![](dotnetimages/collapse.gif)Remarks

Marking a component as requiring generation clears the generating, generated, and failed fields.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupReleasedComponents Class](topic3238.md)   
[GroupReleasedComponents Members](topic3239.md)

©2024 DriveWorks Ltd. All Rights Reserved.
