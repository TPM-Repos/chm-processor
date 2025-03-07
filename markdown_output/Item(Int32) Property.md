Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(Int32) Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) > [Item Property](topic11483.md) : Item(Int32) Property  
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
    ) As [SpecificationMacro](topic11429.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim index As Integer
    Dim value As [SpecificationMacro](topic11429.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [SpecificationMacro](topic11429.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the item to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)   
[Overload List](topic11483.md)


