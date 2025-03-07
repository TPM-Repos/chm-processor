Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileSavePostNotifyEventArgs Constructor   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [FileSavePostNotifyEventArgs Class](topic13661.md) : FileSavePostNotifyEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_saveType_
    Type of save as defined in swFileSaveTypes_e.

_filename_
    The name of the file that was saved.

Glossary Item Box

Creates a new instance of the [FileSavePostNotifyEventArgs](topic13661.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _saveType_ As Integer, _
       ByVal _filename_ As String _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim saveType As Integer
    Dim filename As String
     
    Dim instance As New [FileSavePostNotifyEventArgs](topic13661.md)(saveType, filename)  
  
C#|   
---|---  
      
    
    public FileSavePostNotifyEventArgs( 
       int _saveType_ ,
       string _filename_
    )  
  
#### Parameters

 _saveType_
    Type of save as defined in swFileSaveTypes_e.
_filename_
    The name of the file that was saved.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileSavePostNotifyEventArgs Class](topic13661.md)   
[FileSavePostNotifyEventArgs Members](topic13662.md)


