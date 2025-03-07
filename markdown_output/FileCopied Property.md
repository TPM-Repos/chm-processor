Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FileCopied Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FileCopyingEventArgs Class](topic2859.md) : FileCopied Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether the file has been copied or not. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property FileCopied As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FileCopyingEventArgs](topic2859.md)
    Dim value As Boolean
     
    instance.FileCopied = value
     
    value = instance.FileCopied  
  
C#|   
---|---  
      
    
    public bool FileCopied {get; set;}  
  
# Remarks

If the value of this property is False after the event has been raised, DriveWorks will copy the file using standard procedures.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FileCopyingEventArgs Class](topic2859.md)   
[FileCopyingEventArgs Members](topic2860.md)


