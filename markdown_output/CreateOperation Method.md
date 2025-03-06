![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateOperation Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11101.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : CreateOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The unique name of the operation.

Glossary Item Box

Creates and returns a new operation with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateOperation( _
       ByVal _name_ As String _
    ) As [Operation](topic11068.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim name As String
    Dim value As [Operation](topic11068.md)
     
    value = instance.CreateOperation(name)  
  
C#|   
---|---  
      
    
    public [Operation](topic11068.md) CreateOperation( 
       string _name_
    )  
  
#### Parameters

 _name_
    The unique name of the operation.

# ![](dotnetimages/collapse.gif)Remarks

Multiple operations can share the same title and been hidden/shown based on conditions to allow operations which are conceptually similar but with different semantics based on the environment state.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)

©2024 DriveWorks Ltd. All Rights Reserved.
