Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopiedFile Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISpecificationFileCopyService Interface](topic2316.md) : CopiedFile Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a file has been copied using [CopyFile(String,String)](topic2326.md) method. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event CopiedFile As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFileCopyService](topic2316.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.CopiedFile, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> CopiedFile  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationFileCopyService Interface](topic2316.md)   
[ISpecificationFileCopyService Members](topic2317.md)


