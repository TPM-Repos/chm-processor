Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FinalUploadedFilePath Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [TinyMCEControl Class](topic9204.md) : FinalUploadedFilePath Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the resulting file path of the file after saving. Is converted to a resource URL in the adapter, consumed by the client, then reset until the next upload. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FinalUploadedFilePath As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TinyMCEControl](topic9204.md)
    Dim value As String
     
    value = instance.FinalUploadedFilePath  
  
C#|   
---|---  
      
    
    public string FinalUploadedFilePath {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TinyMCEControl Class](topic9204.md)   
[TinyMCEControl Members](topic9205.md)


