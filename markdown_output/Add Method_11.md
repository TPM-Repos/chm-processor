Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedLayerCollection Class](topic14295.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the layer to add.

Glossary Item Box

Adds a new layer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String _
    ) As [CapturedLayer](topic14288.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedLayerCollection](topic14295.md)
    Dim name As String
    Dim value As [CapturedLayer](topic14288.md)
     
    value = instance.Add(name)  
  
C#|   
---|---  
      
    
    public [CapturedLayer](topic14288.md) Add( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the layer to add.

#### Return Value

The newly created layer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedLayerCollection Class](topic14295.md)   
[CapturedLayerCollection Members](topic14296.md)


