![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
WarningOutput Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6998.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeWithStatus Class](topic6990.md) : WarningOutput Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the end point that allows logical navigation connections to be made from this node when this node produces a warning as it's state. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property WarningOutput As [NodeNavigationOutput](topic7067.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeWithStatus](topic6990.md)
    Dim value As [NodeNavigationOutput](topic7067.md)
     
    value = instance.WarningOutput  
  
C#|   
---|---  
      
    
    public [NodeNavigationOutput](topic7067.md) WarningOutput {get;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This end point can be mapped to a [NodeNavigationInput](topic7058.md) to set up the order in which the nodes will execute.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExecutableNodeWithStatus Class](topic6990.md)   
[ExecutableNodeWithStatus Members](topic6991.md)

©2024 DriveWorks Ltd. All Rights Reserved.
