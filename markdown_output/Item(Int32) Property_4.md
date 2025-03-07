Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(Int32) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureCollection Class](topic14887.md) > [Item Property](topic14900.md) : Item(Int32) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    The index of the item to retrieve.

Glossary Item Box

Gets the item at the specified index. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _index_ As Integer _
    ) As [ReleasedFeature](topic14875.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureCollection](topic14887.md)
    Dim index As Integer
    Dim value As [ReleasedFeature](topic14875.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ReleasedFeature](topic14875.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the item to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFeatureCollection Class](topic14887.md)   
[ReleasedFeatureCollection Members](topic14888.md)   
[Overload List](topic14900.md)


