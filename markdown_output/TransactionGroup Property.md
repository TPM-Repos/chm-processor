       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransactionGroup Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1148.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ViewControl Class](topic1119.md) : TransactionGroup Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The group that will be used for this view control's transaction collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property TransactionGroup As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ViewControl](topic1119.md)
    Dim value As String
     
    value = instance.TransactionGroup  
  
C#|   
---|---  
      
    
    public string TransactionGroup {get;}  
  
# Remarks

This defaults to [ViewName](topic1151.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ViewControl Class](topic1119.md)   
[ViewControl Members](topic1120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
