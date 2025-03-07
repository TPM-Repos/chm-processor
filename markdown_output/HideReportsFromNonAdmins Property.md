Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HideReportsFromNonAdmins Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GeneralGroupSettings Class](topic2940.md) : HideReportsFromNonAdmins Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether reports should be hidden from non-adminstrators. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property HideReportsFromNonAdmins As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GeneralGroupSettings](topic2940.md)
    Dim value As Boolean
     
    instance.HideReportsFromNonAdmins = value
     
    value = instance.HideReportsFromNonAdmins  
  
C#|   
---|---  
      
    
    public bool HideReportsFromNonAdmins {get; set;}  
  
# Remarks

If this is accessed by a non-administrator then an System.UnauthorizedAccessException will be thrown.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GeneralGroupSettings Class](topic2940.md)   
[GeneralGroupSettings Members](topic2941.md)


