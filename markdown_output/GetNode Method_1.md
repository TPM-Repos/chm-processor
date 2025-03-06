![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNode Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13147.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [StartNodeRef Class](topic13140.md) : GetNode Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetNode( _
       ByVal _project_ As [Project](topic3859.md) _
    ) As [IFlowNode](topic6873.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [StartNodeRef](topic13140.md)
    Dim project As [Project](topic3859.md)
    Dim value As [IFlowNode](topic6873.md)
     
    value = instance.GetNode(project)  
  
C#|   
---|---  
      
    
    public override [IFlowNode](topic6873.md) GetNode( 
       [Project](topic3859.md) _project_
    )  
  
#### Parameters

 _project_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StartNodeRef Class](topic13140.md)   
[StartNodeRef Members](topic13141.md)

©2024 DriveWorks Ltd. All Rights Reserved.
