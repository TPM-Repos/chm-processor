       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SearchStartedEventArgs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [SearchStartedEventArgs Class](topic10326.md) : SearchStartedEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_names_
    The names we are searching for.

Glossary Item Box

Initializes a new instance of the [SearchStartedEventArgs](topic10326.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _names_() As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim names() As String
     
    Dim instance As New [SearchStartedEventArgs](topic10326.md)(names)  
  
C#|   
---|---  
      
    
    public SearchStartedEventArgs( 
       string[] _names_
    )  
  
#### Parameters

 _names_
    The names we are searching for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SearchStartedEventArgs Class](topic10326.md)   
[SearchStartedEventArgs Members](topic10327.md)


