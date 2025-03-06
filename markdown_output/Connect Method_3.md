![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Connect Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7064.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeNavigationInput Class](topic7058.md) : Connect Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_output_
    The condition output to map this input to.

Glossary Item Box

Create a connection between this input and the given [NodeOutput](topic7074.md), scheduling the [IFlowNode](topic6873.md) that owns this input to be executed if the mapped output is fulfilled during execution. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Sub Connect( _
       ByVal _output_ As [NodeOutput](topic7074.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeNavigationInput](topic7058.md)
    Dim output As [NodeOutput](topic7074.md)
     
    instance.Connect(output)  
  
C#|   
---|---  
      
    
    public override void Connect( 
       [NodeOutput](topic7074.md) _output_
    )  
  
#### Parameters

 _output_
    The condition output to map this input to.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| output is not a [ConditionOutput](topic6901.md) or a [NodeNavigationOutput](topic7067.md).  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeNavigationInput Class](topic7058.md)   
[NodeNavigationInput Members](topic7059.md)

©2024 DriveWorks Ltd. All Rights Reserved.
