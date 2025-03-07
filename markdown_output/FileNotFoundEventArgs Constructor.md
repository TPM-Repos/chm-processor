Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileNotFoundEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [FileNotFoundEventArgs Class](topic827.md) : FileNotFoundEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fileName_
    The path to the file which is missing.

Glossary Item Box

Initializes a new instance of the [FileNotFoundEventArgs](topic827.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _fileName_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim fileName As String
     
    Dim instance As New [FileNotFoundEventArgs](topic827.md)(fileName)  
  
C#|   
---|---  
      
    
    public FileNotFoundEventArgs( 
       string _fileName_
    )  
  
#### Parameters

 _fileName_
    The path to the file which is missing.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileNotFoundEventArgs Class](topic827.md)   
[FileNotFoundEventArgs Members](topic828.md)


