Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyingSpecificationFile Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : CopyingSpecificationFile Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised before a file for the current specification is copied to its target location. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CopyingSpecificationFile As EventHandler(Of FileCopyingEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of FileCopyingEventArgs)
     
    AddHandler instance.CopyingSpecificationFile, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<FileCopyingEventArgs> CopyingSpecificationFile  
  
# Event Data

The event handler receives an argument of type [FileCopyingEventArgs](topic2859.md) containing data related to this event. The following **FileCopyingEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[FileCopied](topic2866.md)| Gets/sets whether the file has been copied or not.   
[OverWrite](topic2867.md)| Gets whether the target file should be overwritten if it exists.   
[SourcePath](topic2868.md)| Gets the path to the source file that should be copied.   
[TargetPath](topic2869.md)| Gets the path the source file should be copied to.   
  
# Remarks

This event will get raised for every file that is copied as a part of the specification.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


