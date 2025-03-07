Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFormatCollection Class](topic14249.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the additional file format.

Glossary Item Box

Adds a new format to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String _
    ) As [CapturedFormat](topic14240.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFormatCollection](topic14249.md)
    Dim name As String
    Dim value As [CapturedFormat](topic14240.md)
     
    value = instance.Add(name)  
  
C#|   
---|---  
      
    
    public [CapturedFormat](topic14240.md) Add( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the additional file format.

#### Return Value

The newly created format.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFormatCollection Class](topic14249.md)   
[CapturedFormatCollection Members](topic14250.md)


