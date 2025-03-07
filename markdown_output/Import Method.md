Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Import Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) : Import Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serializedForm_
    A serialized team list.

Glossary Item Box

Imports a team list from it's serialized representation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Import( _
       ByVal _serializedForm_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim serializedForm As String
     
    instance.Import(serializedForm)  
  
C#|   
---|---  
      
    
    public void Import( 
       string _serializedForm_
    )  
  
#### Parameters

 _serializedForm_
    A serialized team list.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)


