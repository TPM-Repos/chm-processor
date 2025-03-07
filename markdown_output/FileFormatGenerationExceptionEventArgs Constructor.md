Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileFormatGenerationExceptionEventArgs Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [FileFormatGenerationExceptionEventArgs Class](topic15210.md) : FileFormatGenerationExceptionEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_targetPath_
    The target path.

_exception_
    The exception.

Glossary Item Box

Initializes a new instance of the [FileFormatGenerationExceptionEventArgs](topic15210.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _targetPath_ As String, _
       ByVal _exception_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim targetPath As String
    Dim exception As Exception
     
    Dim instance As New [FileFormatGenerationExceptionEventArgs](topic15210.md)(targetPath, exception)  
  
C#|   
---|---  
      
    
    public FileFormatGenerationExceptionEventArgs( 
       string _targetPath_ ,
       Exception _exception_
    )  
  
#### Parameters

 _targetPath_
    The target path.
_exception_
    The exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileFormatGenerationExceptionEventArgs Class](topic15210.md)   
[FileFormatGenerationExceptionEventArgs Members](topic15211.md)


