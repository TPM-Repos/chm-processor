RemapFolderStatus Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : RemapFolderStatus Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Presents the status of a [DriveWorks.GroupMaintenance.RemapGroupContentFolderAction](topic9959.md) or [DriveWorks.GroupMaintenance.RemapSpecificationFolderAction](topic9970.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum RemapFolderStatus 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemapFolderStatus](topic2360.md)  
  
C#|   
---|---  
      
    
    public enum RemapFolderStatus : System.Enum   
  
# Members

Member| Description  
---|---  
**FolderDifferent**|  The folder has been updated.  
**FolderMissing**|  The folder has not been changed as it was not specified in the source group.  
**FolderSame**|  The folder has not been changed.  
**Unknown**|  The default status.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.RemapFolderStatus**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks Namespace](topic2159.md)


