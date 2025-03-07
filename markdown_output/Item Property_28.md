Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectBreakLineCollection Class](topic14453.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the break-line to get.

Glossary Item Box

Gets the break-line at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectBreakLine](topic14444.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectBreakLineCollection](topic14453.md)
    Dim index As Integer
    Dim value As [ProjectBreakLine](topic14444.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectBreakLine](topic14444.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    The index of the break-line to get.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectBreakLineCollection Class](topic14453.md)   
[ProjectBreakLineCollection Members](topic14454.md)


