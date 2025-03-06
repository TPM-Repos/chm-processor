       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UserDetails Class   
[Members](topic10741.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10740.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) : UserDetails Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a registered user in a DriveWorks group. 

# Object Model

![](dotnetdiagramimages/image542.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public NotInheritable Class UserDetails   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [UserDetails](topic10740.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public sealed class UserDetails   
  
# Remarks

Modifications made to an instance of UserDetails are not immediately reflected in the group from which the instance was obtained. To apply any modifications, call the [DriveWorks.GroupSecurity.TryUpdateUser](topic3338.md) method.

# Inheritance Hierarchy

System.Object  
**DriveWorks.Security.UserDetails**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UserDetails Members](topic10741.md)   
[DriveWorks.Security Namespace](topic10574.md)

©2024 DriveWorks Ltd. All Rights Reserved.
