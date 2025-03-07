Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedBreakLineCollection Class](topic14792.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the break-line to retrieve.

Glossary Item Box

Gets the break-line at the given index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ReleasedBreakLine](topic14782.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedBreakLineCollection](topic14792.md)
    Dim index As Integer
    Dim value As [ReleasedBreakLine](topic14782.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedBreakLine](topic14782.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the break-line to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedBreakLineCollection Class](topic14792.md)   
[ReleasedBreakLineCollection Members](topic14793.md)


