![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11533.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationTaskList Class](topic11525.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The key of the task list entry to retrieve.

Glossary Item Box

Gets the task list entry with the specified key. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _key_ As Object _
    ) As [SpecificationTaskListEntry](topic11537.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [SpecificationTaskList](topic11525.md)
    Dim key As Object
    Dim value As [SpecificationTaskListEntry](topic11537.md)
     
    value = instance.Item(key)  
  
C#|   
---|---  
      
    
    public [SpecificationTaskListEntry](topic11537.md) this[ 
       object _key_
    ]; {get;}  
  
#### Parameters

 _key_
    The key of the task list entry to retrieve.

#### Property Value

The task list entry with the given key, or a null reference if one does not exist.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[SpecificationTaskList Class](topic11525.md)   
[SpecificationTaskList Members](topic11526.md)

©2024 DriveWorks Ltd. All Rights Reserved.
