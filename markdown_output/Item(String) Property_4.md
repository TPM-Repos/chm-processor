Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item(String) Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedFeatureCollection Class](topic14887.md) > [Item Property](topic14900.md) : Item(String) Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the feature to retrieve.

Glossary Item Box

Gets the feature with the specified address 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads ReadOnly Property Item( _
       ByVal _address_ As String _
    ) As [ReleasedFeature](topic14875.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedFeatureCollection](topic14887.md)
    Dim address As String
    Dim value As [ReleasedFeature](topic14875.md)
     
    value = instance.Item(address)  
  
C#|   
---|---  
      
    
    public [ReleasedFeature](topic14875.md) Item( 
       string _address_
    ) {get;}  
  
#### Parameters

 _address_
    The address of the feature to retrieve.

# Remarks

This property performs a linear search of the features, looking for one with the specified address, and thus has O(N) worst case running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedFeatureCollection Class](topic14887.md)   
[ReleasedFeatureCollection Members](topic14888.md)   
[Overload List](topic14900.md)


