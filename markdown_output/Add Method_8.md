Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFeatureParameterCollection Class](topic14225.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the parameter.

Glossary Item Box

Adds a new feature parameter to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _address_ As String _
    ) As [CapturedFeatureParameter](topic14218.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFeatureParameterCollection](topic14225.md)
    Dim address As String
    Dim value As [CapturedFeatureParameter](topic14218.md)
     
    value = instance.Add(address)  
  
C#|   
---|---  
      
    
    public [CapturedFeatureParameter](topic14218.md) Add( 
       string _address_
    )  
  
#### Parameters

 _address_
    The address of the parameter.

#### Return Value

The newly created parameter.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFeatureParameterCollection Class](topic14225.md)   
[CapturedFeatureParameterCollection Members](topic14226.md)


