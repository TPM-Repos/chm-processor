Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(Int32) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) > [Item Property](topic4843.md) : Item(Int32) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to get.

Glossary Item Box

Gets the item at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectSpecificationProperty](topic4853.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim index As Integer
    Dim value As [ProjectSpecificationProperty](topic4853.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectSpecificationProperty](topic4853.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the item to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)   
[Overload List](topic4843.md)


