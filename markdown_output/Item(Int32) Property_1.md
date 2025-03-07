Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(Int32) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFeatureCollection Class](topic14201.md) > [Item Property](topic14215.md) : Item(Int32) Property  
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
    ) As [CapturedFeature](topic14191.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFeatureCollection](topic14201.md)
    Dim index As Integer
    Dim value As [CapturedFeature](topic14191.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [CapturedFeature](topic14191.md) Item( 
       int _index_
    ) {get;}  
  
#### Parameters

 _index_
    The index of the item to retrieve.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFeatureCollection Class](topic14201.md)   
[CapturedFeatureCollection Members](topic14202.md)   
[Overload List](topic14215.md)


