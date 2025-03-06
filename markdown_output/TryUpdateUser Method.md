       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryUpdateUser Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3338.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TryUpdateUser Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_userDetails_
    The information which describes the user to be updated.

Glossary Item Box

Updates an existing user with the specified information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryUpdateUser( _
       ByVal _userDetails_ As [UserDetails](topic10740.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim userDetails As [UserDetails](topic10740.md)
    Dim value As Boolean
     
    value = instance.TryUpdateUser(userDetails)  
  
C#|   
---|---  
      
    
    public bool TryUpdateUser( 
       [UserDetails](topic10740.md) _userDetails_
    )  
  
#### Parameters

 _userDetails_
    The information which describes the user to be updated.

#### Return Value

True if the user is found and updated, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
