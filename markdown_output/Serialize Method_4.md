       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Serialize Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5109.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ReleasedEmail Class](topic5098.md) : Serialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Serializes the information about the email. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Serialize() As Byte()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedEmail](topic5098.md)
    Dim value() As Byte
     
    value = instance.Serialize()  
  
C#|   
---|---  
      
    
    public byte[] Serialize()  
  
#### Return Value

A byte array representing the serialized email information.

# Remarks

This is to be stored in the group as the Data field for a SpecificationDeferredTask.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedEmail Class](topic5098.md)   
[ReleasedEmail Members](topic5099.md)

©2024 DriveWorks Ltd. All Rights Reserved.
