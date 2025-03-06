ShowExceptionDialog Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IWebHostExceptionListener Interface](topic607.md) : ShowExceptionDialog Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The file path to an existing exception report which should be submitted.

Glossary Item Box

Displays an ExceptionReportDialog in the host application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ShowExceptionDialog( _
       ByVal _path_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IWebHostExceptionListener](topic607.md)
    Dim path As String
     
    instance.ShowExceptionDialog(path)  
  
C#|   
---|---  
      
    
    void ShowExceptionDialog( 
       string _path_
    )  
  
#### Parameters

 _path_
    The file path to an existing exception report which should be submitted.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IWebHostExceptionListener Interface](topic607.md)   
[IWebHostExceptionListener Members](topic608.md)


