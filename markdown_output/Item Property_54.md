![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4170.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentTasks Class](topic4163.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The unique identifier of the collection to retrieve.

Glossary Item Box

Gets the collection with the given key. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _key_ As String _
    ) As [ComponentTaskAccessor](topic6429.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentTasks](topic4163.md)
    Dim key As String
    Dim value As [ComponentTaskAccessor](topic6429.md)
     
    value = instance.Item(key)  
  
C#|   
---|---  
      
    
    public [ComponentTaskAccessor](topic6429.md) this[ 
       string _key_
    ]; {get;}  
  
#### Parameters

 _key_
    The unique identifier of the collection to retrieve.

#### Property Value

The accessor that provides access to the collection associated with the specified key, or a null reference (Nothing in VB) if the accessor does not exist.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectComponentTasks Class](topic4163.md)   
[ProjectComponentTasks Members](topic4164.md)

©2024 DriveWorks Ltd. All Rights Reserved.
