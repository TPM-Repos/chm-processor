Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedLayerCollection Class](topic14976.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the layer to add.

_visibility_
    The value of the visibility parameter.

Glossary Item Box

Adds a new layer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _visibility_ As String _
    ) As [ReleasedLayer](topic14968.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedLayerCollection](topic14976.md)
    Dim name As String
    Dim visibility As String
    Dim value As [ReleasedLayer](topic14968.md)
     
    value = instance.Add(name, visibility)  
  
C#|   
---|---  
      
    
    public [ReleasedLayer](topic14968.md) Add( 
       string _name_ ,
       string _visibility_
    )  
  
#### Parameters

 _name_
    The name of the layer to add.
_visibility_
    The value of the visibility parameter.

#### Return Value

The newly created layer.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedLayerCollection Class](topic14976.md)   
[ReleasedLayerCollection Members](topic14977.md)


