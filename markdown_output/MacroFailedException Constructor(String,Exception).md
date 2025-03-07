Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MacroFailedException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [MacroFailedException Class](topic3675.md) > [MacroFailedException Constructor](topic3681.md) : MacroFailedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    

_inner_
    

Glossary Item Box

Creates a new [MacroFailedException](topic3675.md) object. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As String
    Dim inner As Exception
     
    Dim instance As New [MacroFailedException](topic3675.md)(message, inner)  
  
C#|   
---|---  
      
    
    public MacroFailedException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    
_inner_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[MacroFailedException Class](topic3675.md)   
[MacroFailedException Members](topic3676.md)   
[Overload List](topic3681.md)


