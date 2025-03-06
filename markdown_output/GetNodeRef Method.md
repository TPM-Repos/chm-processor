![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNodeRef Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12908.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [NodeCollectionRef Class](topic12900.md) : GetNodeRef Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the node to reference.

Glossary Item Box

Gets a reference to the node at the given index. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetNodeRef( _
       ByVal _index_ As Integer _
    ) As [ExecutableNodeRef](topic12864.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeCollectionRef](topic12900.md)
    Dim index As Integer
    Dim value As [ExecutableNodeRef](topic12864.md)
     
    value = instance.GetNodeRef(index)  
  
C#|   
---|---  
      
    
    public abstract [ExecutableNodeRef](topic12864.md) GetNodeRef( 
       int _index_
    )  
  
#### Parameters

 _index_
    The index of the node to reference.

#### Return Value

A reference to the node.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeCollectionRef Class](topic12900.md)   
[NodeCollectionRef Members](topic12901.md)

©2024 DriveWorks Ltd. All Rights Reserved.
