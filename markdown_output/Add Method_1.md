Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedAlternativeCollection Class](topic14039.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the alternative.

_path_
    The path to the alternative file.

Glossary Item Box

Adds and returns a new alternative. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _path_ As String _
    ) As [CapturedAlternative](topic14031.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedAlternativeCollection](topic14039.md)
    Dim name As String
    Dim path As String
    Dim value As [CapturedAlternative](topic14031.md)
     
    value = instance.Add(name, path)  
  
C#|   
---|---  
      
    
    public [CapturedAlternative](topic14031.md) Add( 
       string _name_ ,
       string _path_
    )  
  
#### Parameters

 _name_
    The name of the alternative.
_path_
    The path to the alternative file.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedAlternativeCollection Class](topic14039.md)   
[CapturedAlternativeCollection Members](topic14040.md)


