Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyingFile Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISpecificationFileCopyService Interface](topic2316.md) : CopyingFile Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a file is being copied by the [CopyFile(String,String)](topic2326.md) method. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event CopyingFile As EventHandler(Of FileCopyingEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFileCopyService](topic2316.md)
    Dim handler As EventHandler(Of FileCopyingEventArgs)
     
    AddHandler instance.CopyingFile, handler  
  
C#|   
---|---  
      
    
    event EventHandler<FileCopyingEventArgs> CopyingFile  
  
# Event Data

The event handler receives an argument of type [FileCopyingEventArgs](topic2859.md) containing data related to this event. The following **FileCopyingEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[FileCopied](topic2866.md)| Gets/sets whether the file has been copied or not.   
[OverWrite](topic2867.md)| Gets whether the target file should be overwritten if it exists.   
[SourcePath](topic2868.md)| Gets the path to the source file that should be copied.   
[TargetPath](topic2869.md)| Gets the path the source file should be copied to.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationFileCopyService Interface](topic2316.md)   
[ISpecificationFileCopyService Members](topic2317.md)


