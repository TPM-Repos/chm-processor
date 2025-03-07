Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FailDate Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DeferredTaskFailureDetails Class](topic2666.md) : FailDate Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the date that the failure occurred. This is in the format yyyy-MM-dd HH:mm:ss 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property FailDate As Date  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DeferredTaskFailureDetails](topic2666.md)
    Dim value As Date
     
    value = instance.FailDate  
  
C#|   
---|---  
      
    
    public DateTime FailDate {get;}  
  
# Remarks

If no date has been stored the current date/time will be returned.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DeferredTaskFailureDetails Class](topic2666.md)   
[DeferredTaskFailureDetails Members](topic2667.md)


